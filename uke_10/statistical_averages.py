from collections import Counter

def almost_equals(a, b):
   return abs(a - b) < 0.00000001

#A
def mean(num_list):
    return sum(num_list)/len(num_list)

#B
def median(num_list):
    num_list_sorted = sorted(num_list)
    list_len = len(num_list)
    if list_len % 2 != 0:
        return float(num_list_sorted[list_len // 2])
    else:
        return mean(num_list_sorted[list_len // 2 - 1:list_len // 2 + 1])

#C
def mode(num_list):
    num_list_mod = [float(x) for x in num_list]
    instances = Counter(num_list_mod)
    mode_list = set()
    for num in instances:
        if instances[num] == max(instances.values()):
            mode_list.add(num)
    return ", ".join(str(x) for x in mode_list)

#D
def cmd_main():
    print("Regn ut statistiske gjennomsnitt for en liste.\nOppgi tallene du vil regne ut gjennomsnitt for, separert av mellomrom:")
    num_list_input = list(map(float, input().split(" ")))
    print(f"\nGjennomsnitt: {mean(num_list_input)}\nMedian: {median(num_list_input)}\nTypetall {mode(num_list_input)}")

#If run directly
if __name__ == "__main__":
    cmd_main()