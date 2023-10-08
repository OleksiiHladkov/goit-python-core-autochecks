import random


def get_random_winners(quantity:int, participants:dict) -> list:
    result = []
    
    if quantity > len(participants):
        return result
    
    part_list = list(participants.keys())
    random.shuffle(part_list)
    result = random.sample(part_list, k=quantity)

    return result





if __name__ == "__main__":
    participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
    }
    print(get_random_winners(2, participants))