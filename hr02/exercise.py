'''
Write a single line that would satisfy:
You need to firgure out the total cost of an order.
Subtotal is $10. Discount is 30%. Tax is 5%. 
Shipping is $7.50.
Calculate total in one line, then print the result.
'''
total_price = 10 * (1.0 - 0.3) * (1.0 + 0.05) + 7.50 
print total_price