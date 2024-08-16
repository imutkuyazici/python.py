import random
import os

class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.goals_scored = 0
        self.goals_conceded = 0

    @property
    def goal_difference(self):
        return self.goals_scored - self.goals_conceded

    def update_stats(self, scored, conceded):
        self.goals_scored += scored
        self.goals_conceded += conceded
        if scored > conceded:
            self.points += 3
            self.wins += 1
        elif scored < conceded:
            self.losses += 1
        else:
            self.points += 1
            self.draws += 1

    def __repr__(self):
        return (f"{self.name} (P: {self.points}, W: {self.wins}, L: {self.losses}, "
                f"D: {self.draws}, GS: {self.goals_scored}, GC: {self.goals_conceded}, "
                f"GD: {self.goal_difference})")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome_screen():
    clear_screen()
    print("Şampiyonlar Ligi'ne Hoş Geldiniz")
    print("1. Takım Kaydet")
    print("2. Grupları ve Takımları Görüntüle")
    print("3. Eleme Aşamasını Başlat")
    print("4. Çıkış")

def get_teams():
    teams = {}
    while len(teams) < 32:
        team_name = input(f"Takım {len(teams) + 1}: ").strip()
        if team_name in teams:
            print("Hata: Bu takım zaten girilmiş. Lütfen farklı bir takım girin.")
        else:
            teams[team_name] = Team(team_name)
    return list(teams.values())

def distribute_groups(teams):
    random.shuffle(teams)
    groups = {f'Grup {i+1}': [] for i in range(8)}
    for i, team in enumerate(teams):
        group_number = i // 4 + 1
        groups[f'Grup {group_number}'].append(team)
    return groups

def display_groups(groups):
    clear_screen()
    for group, teams in groups.items():
        print(f"{group}:")
        for team in teams:
            print(f"  {team}")

def display_group_standings(teams):
    clear_screen()
    sorted_teams = sorted(teams, key=lambda t: (t.points, t.goal_difference, t.goals_scored), reverse=True)
    for team in sorted_teams:
        print(team)
    print("\n")  # Add an extra line for readability

def play_match(team1, team2):
    score1 = random.randint(0, 5)
    score2 = random.randint(0, 5)
    print(f"{team1.name} {score1} - {score2} {team2.name}")
    team1.update_stats(score1, score2)
    team2.update_stats(score2, score1)

def play_group_matches(groups):
    for group, teams in groups.items():
        print(f"{group} Maçları")
        for i in range(len(teams)):
            for j in range(i + 1, len(teams)):
                input(f"{teams[i].name} ile {teams[j].name} arasındaki maçı başlatmak için Enter'a basın...")
                play_match(teams[i], teams[j])
                print("\n" * 3)  # Maç sonucu arası boşluk
        display_group_standings(teams)
        input("Devam etmek için Enter'a basın...")
        clear_screen()

def get_sorted_teams(teams):
    return sorted(teams, key=lambda t: (t.points, t.goal_difference, t.goals_scored), reverse=True)

def start_knockout_stage(teams):
    # Placeholder function for knockout stages
    print("Eleme aşamaları başlatıldı. (Bu kısım daha sonra eklenecek)")

def main():
    teams = []
    groups = {}
    
    while True:
        print_welcome_screen()
        choice = input("Seçiminizi yapın (1/2/3/4): ").strip()
        if choice == '1':
            teams = get_teams()
            groups = distribute_groups(teams)
            clear_screen()
        elif choice == '2':
            if groups:
                display_groups(groups)
            else:
                print("Gruplar oluşturulmadı.")
            input("Devam etmek için Enter'a basın...")
            clear_screen()
        elif choice == '3':
            if groups:
                play_group_matches(groups)
                sorted_teams = []
                for teams in groups.values():
                    sorted_teams.extend(get_sorted_teams(teams))
                start_knockout_stage(sorted_teams)
            else:
                print("Gruplar oluşturulmadı.")
            input("Devam etmek için Enter'a basın...")
            clear_screen()
        elif choice == '4':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
            input("Devam etmek için Enter'a basın...")
            clear_screen()

if __name__ == "__main__":
    main()
   