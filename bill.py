def calculate_remaining_due(total_bill, amount_paid):
    

    remaining_due = total_bill - amount_paid
    
    
    if remaining_due <= 0:
        return 0
    else:
        return remaining_due

total_bill_1 = 150.75
amount_paid_1 = 100.00
remaining_1 = calculate_remaining_due(total_bill_1, amount_paid_1)
print(f"Total Bill: ${total_bill_1}")
print(f"Amount Paid: ${amount_paid_1}")
print(f"Remaining Due: ${remaining_1}\n")