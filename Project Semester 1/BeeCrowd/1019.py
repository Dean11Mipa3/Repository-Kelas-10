second = int(input())
minute = int(second/60)
second -= minute*60
hour = int(minute/60)
minute -= hour*60

print(f"{hour}:{minute}:{second}")