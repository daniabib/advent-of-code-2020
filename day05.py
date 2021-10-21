PASS_EXAMPLE = "FBFBBFFRLR"


class BoardingPass:
    rows: int = 128
    cols: int = 8

    def __init__(self, seat_phrase: str) -> None:
        self.seat_phrase = seat_phrase
        self.row_code = self.seat_phrase[:7]
        self.col_code = self.seat_phrase[7:]


def find_row(boarding_pass: BoardingPass) -> int:
    low: int = 0
    high: int = boarding_pass.rows
    mid: int = (high + low) // 2

    for letter in boarding_pass.row_code:
        if letter == "F":
            high = mid
            mid = (high + low) // 2
        elif letter == "B":
            low = mid
            mid = (high + low) // 2

    return mid


def find_col(boarding_pass: BoardingPass) -> int:
    low: int = 0
    high: int = boarding_pass.cols
    mid: int = (high + low) // 2

    for letter in boarding_pass.col_code:
        if letter == "L":
            high = mid
            mid = (high + low) // 2
        elif letter == "R":
            low = mid
            mid = (high + low) // 2

    return mid


def find_seatID(boarding_pass: BoardingPass) -> int:
    return find_row(boarding_pass) * 8 + find_col(boarding_pass)


assert find_row(BoardingPass(PASS_EXAMPLE)) == 44
assert find_col(BoardingPass(PASS_EXAMPLE)) == 5
assert find_seatID(BoardingPass(PASS_EXAMPLE)) == 357

if __name__ == "__main__":
    with open("inputs/day05.txt") as f:
        seat_ids = [find_seatID(BoardingPass(line)) for line in f]
        # Part 1
        print(f"Part 1 - Max seat ID: {max(seat_ids)}")
        # Part 2
        seat_ids.sort()
        for i in range(seat_ids[0], seat_ids[-1]+1):
           if i not in seat_ids:
                print(f"Part 2 - My seat ID: {i}")