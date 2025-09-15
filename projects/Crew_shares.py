#JC 2nd Crew shares

Money = input("How much money does the ship have:")
crew_count = input("how many crew members are there:")
crew_count = int(crew_count)
Money = int(Money)
print(crew_count)



Share_Value = (Money / (crew_count + 10))
crew_share = (Share_Value - 500)
captian_shares = (Share_Value * 7)
First_mate_shares = (Share_Value * 3)
print(f"The crew still need to get payed {crew_share:.2f}")
print(f"The captain got {captian_shares:.2F}")
print(f"The first mate got {First_mate_shares:.2f}")