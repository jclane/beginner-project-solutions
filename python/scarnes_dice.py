from random import choice as rchoice


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def increase_score(self, value):
        self.score = self.score + value


class Game:

    def __init__(self):
        self.players = []
        self.current_roll = 0
        self.game_over = False
        self.get_players()

    def get_players(self):
        resp = "potato"
        while not resp.isdigit():
            resp = self.get_input("\nHow many players are there?")
        num_of_players = int(resp)
        for num in range(0, num_of_players):
            name = ""
            while not name:
                name = self.get_input("Enter name for Player {}".format(str(num)))
            self.players.append(Player(name))
        self.start_game()

    def roll_dice(self):
        return rchoice([1, 2, 3, 4, 5, 6])

    def get_next_player(self):
        next_index = self.players.index(self.current_player) + 1
        if next_index > len(self.players) - 1:
            next_index = 0
        return self.players[next_index]

    def show_scores(self):
        longest = 0
        for player in self.players:
            if len(player.name) > longest:
                longest = len(player.name)

        print("\n\t{: ^15}\n".format("Scoreboard"))
        for player in self.players:
            row = [player.name, player.score]
            print("\t{: ^10} {: ^10}".format(*row))
        print("")

    def get_input(self, msg):
        resp = input("{} >> ".format(msg))
        if resp in ["score"]:
            self.show_scores()
        return resp

    def end_turn(self):
        if self.current_player.score >= 100:
            self.game_over = True
        else:
            print("\n{}'s final score: {}".format(self.current_player.name,
                                                  self.current_player.score))
            print("Ending turn...")
            self.current_player = self.get_next_player()

    def begin_turn(self):
        print("\n{}'s turn:".format(self.current_player.name))
        original_score = self.current_player.score
        score = self.current_player.score
        keep_rolling = True
        while keep_rolling:
            self.current_roll = self.roll_dice()
            print("\n\tCurrent score: {}\n".format(score))
            print("\t{} rolled {}".format(self.current_player.name,
                                          self.current_roll))
            if self.current_roll > 1:
                score = score + self.current_roll
                resp = ""
                while resp.lower() not in ["yes", "no", "y", "n"]:
                    resp = self.get_input("\tKeep rolling?")
                if resp.lower() in ["no", "n"]:
                    self.current_player.score = score
                    keep_rolling = False
            else:
                self.current_player.score = original_score
                keep_rolling = False

    def start_game(self):
        self.current_player = rchoice(self.players)
        while not self.game_over:
            self.begin_turn()
            self.end_turn()



game = Game()
