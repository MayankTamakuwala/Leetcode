SELECT ROUND(SUM(mul)/SUM(order_occurrences),2) as average_items_per_order FROM (
    SELECT item_count, order_occurrences, (item_count * order_occurrences) AS mul FROM Orders
) as Mul_Table
