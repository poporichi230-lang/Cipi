import random
import time
import os

# ─── CULORI ANSI ────────────────────────────────────────────────────────────
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def pause(msg="Apasa Enter pentru a continua..."):
    input(f"\n{YELLOW}{msg}{RESET}")


# ─── ETAPA 1: CLASA JUCATORULUI ──────────────────────────────────────────────
class Player:
    def __init__(self, name):
        self.name   = name
        self.hp     = 100
        self.max_hp = 100
        self.attack = 15
        self.defense = 5
        self.level  = 1
        self.xp     = 0
        self.xp_needed = 30
        self.gold   = 10
        self.inventory = []
        self.potions = 2

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        actual = max(1, dmg - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual

    def heal(self, amount):
        healed = min(amount, self.max_hp - self.hp)
        self.hp += healed
        return healed

    def use_potion(self):
        if self.potions > 0:
            restored = self.heal(40)
            self.potions -= 1
            return restored
        return 0

    def gain_xp(self, amount):
        self.xp += amount
        leveled = False
        while self.xp >= self.xp_needed:
            self.xp -= self.xp_needed
            self.level += 1
            self.xp_needed = int(self.xp_needed * 1.5)
            self.max_hp += 20
            self.hp = self.max_hp
            self.attack += 5
            self.defense += 2
            leveled = True
        return leveled

    def status(self):
        hp_pct = self.hp / self.max_hp
        bar_len = 20
        filled  = int(bar_len * hp_pct)
        color   = GREEN if hp_pct > 0.5 else (YELLOW if hp_pct > 0.25 else RED)
        bar     = color + "█" * filled + RESET + "░" * (bar_len - filled)
        xp_pct  = self.xp / self.xp_needed
        xp_bar  = CYAN + "█" * int(bar_len * xp_pct) + RESET + "░" * (bar_len - int(bar_len * xp_pct))
        print(f"{BOLD}{BLUE}╔══ {self.name} (Nivel {self.level}) ══╗{RESET}")
        print(f"  HP  [{bar}] {self.hp}/{self.max_hp}")
        print(f"  XP  [{xp_bar}] {self.xp}/{self.xp_needed}")
        print(f"  ⚔  ATK={self.attack}  🛡 DEF={self.defense}  🧪 Potiuni={self.potions}  💰 Aur={self.gold}")


# ─── ETAPA 2: CLASA INAMICILOR ───────────────────────────────────────────────
class Enemy:
    TYPES = [
        {"name": "Goblin",      "hp": 30,  "atk": 10, "xp": 12, "gold": (2,6),   "emoji": "👺"},
        {"name": "Schelet",     "hp": 45,  "atk": 14, "xp": 18, "gold": (4,10),  "emoji": "💀"},
        {"name": "Orc",         "hp": 70,  "atk": 18, "xp": 25, "gold": (6,14),  "emoji": "👹"},
        {"name": "Vrajitor",    "hp": 55,  "atk": 22, "xp": 30, "gold": (8,16),  "emoji": "🧙"},
        {"name": "Dragon Mic",  "hp": 120, "atk": 28, "xp": 50, "gold": (15,30), "emoji": "🐉"},
    ]

    def __init__(self, player_level):
        pool = [t for t in self.TYPES if t["xp"] <= 20 + player_level * 12]
        t = random.choice(pool if pool else self.TYPES[:2])
        scale = 1 + (player_level - 1) * 0.15
        self.name   = t["name"]
        self.emoji  = t["emoji"]
        self.hp     = int(t["hp"] * scale)
        self.max_hp = self.hp
        self.attack = int(t["atk"] * scale)
        self.xp_reward  = int(t["xp"] * scale)
        self.gold_reward = random.randint(*t["gold"])

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)
        return dmg

    def status(self):
        pct     = self.hp / self.max_hp
        bar_len = 20
        filled  = int(bar_len * pct)
        color   = GREEN if pct > 0.5 else (YELLOW if pct > 0.25 else RED)
        bar     = color + "█" * filled + RESET + "░" * (bar_len - filled)
        print(f"{BOLD}{RED}╔══ {self.emoji} {self.name} ══╗{RESET}")
        print(f"  HP  [{bar}] {self.hp}/{self.max_hp}  ⚔ ATK={self.attack}")


# ─── ETAPA 3: SISTEMUL DE LUPTA ──────────────────────────────────────────────
def battle(player, enemy):
    print(f"\n{RED}{BOLD}⚔  ATAC! Un {enemy.emoji} {enemy.name} a aparut! ⚔{RESET}\n")
    time.sleep(0.8)

    while player.is_alive() and enemy.is_alive():
        clear()
        print(f"\n{BOLD}{'─'*45}{RESET}")
        player.status()
        print()
        enemy.status()
        print(f"{BOLD}{'─'*45}{RESET}\n")

        print(f"{YELLOW}Ce faci?{RESET}")
        print("  [1] Ataca")
        print("  [2] Foloseste Potiune")
        print("  [3] Fugi")

        choice = input("\n> ").strip()

        if choice == "1":
            # Jucatorul ataca
            crit   = random.random() < 0.15
            base   = random.randint(int(player.attack * 0.8), int(player.attack * 1.2))
            damage = int(base * 1.8) if crit else base
            enemy.take_damage(damage)
            crit_txt = f"{RED} CRITIC!{RESET}" if crit else ""
            print(f"\n{GREEN}Ai lovit {enemy.name} pentru {damage} daune!{crit_txt}{RESET}")

            if not enemy.is_alive():
                break

            # Inamicul contraataca
            e_dmg  = random.randint(int(enemy.attack * 0.7), int(enemy.attack * 1.3))
            actual = player.take_damage(e_dmg)
            print(f"{RED}{enemy.name} te loveste pentru {actual} daune!{RESET}")

        elif choice == "2":
            if player.potions > 0:
                restored = player.use_potion()
                print(f"\n{GREEN}Ai folosit o potiune si ai recuperat {restored} HP!{RESET}")
            else:
                print(f"\n{RED}Nu ai potiuni!{RESET}")

        elif choice == "3":
            if random.random() < 0.45:
                print(f"\n{YELLOW}Ai fugit cu succes!{RESET}")
                pause()
                return "fled"
            else:
                e_dmg  = random.randint(int(enemy.attack * 0.7), int(enemy.attack * 1.3))
                actual = player.take_damage(e_dmg)
                print(f"\n{RED}Nu ai reusit sa fugi! {enemy.name} te loveste pentru {actual} daune!{RESET}")
        else:
            print(f"{RED}Optiune invalida!{RESET}")

        time.sleep(0.9)

    if player.is_alive():
        leveled = player.gain_xp(enemy.xp_reward)
        player.gold += enemy.gold_reward
        print(f"\n{GREEN}{BOLD}Ai invins {enemy.emoji} {enemy.name}!{RESET}")
        print(f"  +{enemy.xp_reward} XP  +{enemy.gold_reward} Aur")
        if leveled:
            print(f"\n{CYAN}{BOLD}🎉 NIVEL NOU! Esti acum Nivel {player.level}! 🎉{RESET}")
            print(f"   HP Max +20 | ATK +5 | DEF +2")
        pause()
        return "win"
    else:
        return "dead"


# ─── ETAPA 4: MAGAZIN ────────────────────────────────────────────────────────
SHOP_ITEMS = [
    {"name": "Potiune Mica",   "cost": 8,  "type": "potion", "amount": 1},
    {"name": "Potiune Mare",   "cost": 18, "type": "potion", "amount": 3},
    {"name": "Sabie Ascutita", "cost": 25, "type": "atk",    "amount": 8},
    {"name": "Scut Greu",      "cost": 20, "type": "def",    "amount": 5},
]

def shop(player):
    while True:
        clear()
        print(f"\n{CYAN}{BOLD}🏪  MAGAZIN  🏪{RESET}")
        print(f"  Aurul tau: {player.gold} 💰\n")
        for i, item in enumerate(SHOP_ITEMS, 1):
            affordable = GREEN if player.gold >= item["cost"] else RED
            print(f"  [{i}] {item['name']:<20} {affordable}{item['cost']} aur{RESET}")
        print(f"\n  [0] Pleaca din magazin")

        choice = input("\n> ").strip()
        if choice == "0":
            break
        if choice.isdigit() and 1 <= int(choice) <= len(SHOP_ITEMS):
            item = SHOP_ITEMS[int(choice) - 1]
            if player.gold >= item["cost"]:
                player.gold -= item["cost"]
                if item["type"] == "potion":
                    player.potions += item["amount"]
                    print(f"\n{GREEN}Ai cumparat {item['name']}! Potiuni: {player.potions}{RESET}")
                elif item["type"] == "atk":
                    player.attack += item["amount"]
                    print(f"\n{GREEN}Ai cumparat {item['name']}! ATK +{item['amount']}{RESET}")
                elif item["type"] == "def":
                    player.defense += item["amount"]
                    print(f"\n{GREEN}Ai cumparat {item['name']}! DEF +{item['amount']}{RESET}")
                time.sleep(0.8)
            else:
                print(f"\n{RED}Nu ai destul aur!{RESET}")
                time.sleep(0.8)


# ─── ETAPA 5: ECRANUL PRINCIPAL ──────────────────────────────────────────────
BANNER = f"""
{CYAN}{BOLD}
  ██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗
  ██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗  ██║
  ██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔██╗ ██║
  ██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╗██║
  ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚████║
  ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
                   ⚔  DUNGEON QUEST  ⚔
{RESET}"""

def main():
    clear()
    print(BANNER)
    name = input(f"{YELLOW}Introdu numele eroului tau: {RESET}").strip() or "Erou"
    player = Player(name)

    dungeon_floor = 1
    encounters    = 0
    running       = True

    while running and player.is_alive():
        clear()
        print(f"\n{BOLD}{'═'*45}{RESET}")
        print(f"{CYAN}{BOLD}  Etaj {dungeon_floor} al Dungeonului{RESET}")
        print(f"{BOLD}{'═'*45}{RESET}\n")
        player.status()

        print(f"\n{YELLOW}Ce faci?{RESET}")
        print("  [1] Exploreaza (cauta inamici)")
        print("  [2] Magazin")
        print("  [3] Odihneste-te (+20 HP, cost: 5 aur)")
        print("  [4] Iesi din joc")

        choice = input("\n> ").strip()

        if choice == "1":
            encounters += 1
            enemy  = Enemy(player.level)
            result = battle(player, enemy)
            if result == "dead":
                running = False
            elif result == "win":
                if encounters % 5 == 0:
                    dungeon_floor += 1
                    print(f"\n{CYAN}{BOLD}🏆 Ai ajuns la Etajul {dungeon_floor}! Dusmanii devin mai puternici...{RESET}")
                    pause()

        elif choice == "2":
            shop(player)

        elif choice == "3":
            if player.gold >= 5:
                player.gold -= 5
                restored = player.heal(20)
                print(f"\n{GREEN}Te-ai odihnit si ai recuperat {restored} HP.{RESET}")
                time.sleep(1)
            else:
                print(f"\n{RED}Nu ai 5 aur pentru odihna!{RESET}")
                time.sleep(1)

        elif choice == "4":
            print(f"\n{YELLOW}La revedere, {player.name}!{RESET}\n")
            break

    if not player.is_alive():
        clear()
        print(f"\n{RED}{BOLD}")
        print("  ╔════════════════════════════╗")
        print("  ║        AI MURIT...         ║")
        print("  ╚════════════════════════════╝")
        print(f"{RESET}")
        print(f"  Erou: {player.name}  |  Nivel: {player.level}  |  Etaj: {dungeon_floor}")
        print(f"  Inamici invinsi: {encounters}")
        print()


if __name__ == "__main__":
    main()
