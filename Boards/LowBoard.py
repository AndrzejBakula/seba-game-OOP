
class LowBoard:

    lowBoard_list = []

    def __init__(self):
        with open("Boards/lowboard.txt") as file_in:
            for line in file_in:
                self.lowBoard_list.append(line.split())