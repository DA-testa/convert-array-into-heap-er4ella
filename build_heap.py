# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        maxi = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[maxi] < data[maxi]:
            maxi = left
        if right < n and data[maxi] < data[maxi]:
            maxi = right

        if i != maxi :
            swaps.append((i, maxi))
            data[i], data[maxi] = data[maxi], data[i]

            while maxi * 2 + 1 < n:
                i = maxi
                maxi = 2 * i + 1
                if maxi + 1 < n and data[maxi + 1] < data[maxi]:
                    maxi = maxi + 1

                if data[i] > data[maxi]:
                    swaps.append((i, maxi))
                    data[i], data[maxi] = data[maxi], data[i]
        else:
            j = maxi
            while j * 2 + 1 < n:
                i = j
                j = 2 * i + 1
                if j + 1 < n and data[j+1] < data[j]:
                    j = j + 1
                
                if data[i] > data[j]:
                    swaps.append((i, j))
                    data[i], data[j] = data[j], data[i]
                    i = j
                else:
                    break

    return swaps


def main():
    text=input("F or I: ")
    if "I" in text:
        n=int(input())
        data = list(map(int, input().split()))
    elif "F" in text:
        name=input()
        path='./tests/'
        file = path+name
        if "a" not in name:
            try:
                with open(file) as f:
                    n=int(f.readline())
                    data = list(map(int, f.readline().split()))
            except Exception as e:
                print("Kļūda", str(e))
                return

    assert len(data) == n

    swaps = build_heap(data)

    assert len(swaps) <= 4 * len(data)
    print(len(swaps))

    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
