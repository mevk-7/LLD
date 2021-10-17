from SplitWise.src.split import SplitStrategy, ExactSplit, EqualSplit, PercentSplit
from SplitWise.src.user import User
from SplitWise.src.splitwise import SplitWise

if __name__ == '__main__':
    userA = User("UserA")
    userB = User("UserB")
    userC = User("UserC")
    split_wise = SplitWise()
    split_wise.register_user(userA)
    split_wise.register_user(userB)
    split_wise.register_user(userC)
    print("*"*10)
    split1 = EqualSplit()
    split_wise.add_expense("KFC party", userA, [userB, userC], 600, split1)
    split_wise.print_expense_user(userA)
    split_wise.print_expense_user(userB)
    split_wise.print_expense_user(userC)
    split_wise.print_all_expenses()

    print("*"*10)
    split2 = ExactSplit([200, 300])
    split_wise.add_expense("Birthday", userB, [userC, userA], 500, split2)
    split_wise.print_expense_user(userA)
    split_wise.print_expense_user(userB)
    split_wise.print_expense_user(userC)
    split_wise.print_all_expenses()

    print("*"*10)
    split3 = PercentSplit([70, 30])
    split_wise.add_expense("Drinks", userC, [userA, userA], 1000, split3)
    split_wise.print_expense_user(userA)
    split_wise.print_expense_user(userB)
    split_wise.print_expense_user(userC)
    split_wise.print_all_expenses()
