def solution(n):
    answer = 0
    queen = [[False]*n for _ in range(n)]
    ans = 0

    def check(row, col):
        #현재 퀸이 위치하고 같은 col의 row에 이미 퀸이 있는지 확인한다.
        for i in range(n):
            if row == i:
                # 이 조건이 없으면 항상 False 로 return 되어 Fail됨
                continue
            if queen[i][col]:
                return False

        #왼쪽 상단
        x, y = row-1, col-1
        while x>=0 and y>=0:
            if queen[x][y]:
                return False
            x -= 1
            y -= 1

        #오른쪽 상단
        x, y = row-1, col+1
        while x>=0 and y<n:
            if queen[x][y]:
                return False
            x -= 1
            y += 1

        return True

    def place(row):
        nonlocal answer
        if row == n:
            answer += 1
            return

        for col in range(n):
            queen[row][col] = True
            if check(row, col):
                place(row+1)
            queen[row][col] = False

    place(0)
    return answer