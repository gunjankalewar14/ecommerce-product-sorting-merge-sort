# Case Study 1: E-commerce Product Sorting with Divide and Conquer

**Course:** PCC-201-COM – Data Structures and Algorithms  
**Unit:** I – Introduction to Data Structures and Algorithms  
**Prepared by:** Gunjan Maruti Kalewar · Roll No. 44 · Division B · Batch B

## 1. Abstract

An online store may display hundreds or thousands of products after a customer chooses a category or filter. A useful results page should put items in a consistent order, such as price from low to high. This case study models that task with **merge sort**, a divide-and-conquer sorting algorithm. The product records are divided into smaller parts, each part is sorted, and the sorted parts are merged. The analysis considers ordering, stability, time and memory cost, and the limits of using a simple in-memory sort in a real store.

## 2. Scenario and problem

A customer filters a store to show available headphones and selects **Price: Low to High**. The catalog service receives matching product records. The records can arrive in any order and may have equal prices. The system must return all matching items in ascending price order without losing product details or producing confusing changes in the relative order of equal-price items.

For an illustrative catalog:

| Product | Price (₹) | Rating |
|---|---:|---:|
| Echo Buds | 2,499 | 4.2 |
| SoundGo | 1,999 | 4.4 |
| AirTune | 1,999 | 4.1 |
| BassMax | 3,299 | 4.6 |

The intended result is SoundGo, AirTune, Echo Buds, BassMax. SoundGo and AirTune have the same price, so a **stable** sort keeps their input order unless the store explicitly defines another tie-break rule.

## 3. Data model and algorithm

Each product is a record with at least an ID, name, price, availability, and rating. The selected sort key is price. In a real catalog, the system should define a deterministic secondary key, such as product ID, where stable input order is not an appropriate tie-break.

Merge sort follows these steps:

1. Divide the list into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves by repeatedly taking the smaller current price.
4. Continue until one sorted list contains all matching products.

```text
MERGE-SORT(products):
    if length(products) <= 1:
        return products
    split products into left and right halves
    left_sorted  = MERGE-SORT(left)
    right_sorted = MERGE-SORT(right)
    return MERGE(left_sorted, right_sorted)
```

The application should sort only the records matching the active category and filters. It should keep prices as numeric values (not strings), apply the selected ascending or descending direction, and preserve the complete product record when moving items.

## 4. Complexity and design trade-offs

For `n` matching products, merge sort takes **O(n log n)** time in best, average, and worst cases. A typical array-based implementation uses **O(n)** additional memory for merging. Merge sort is stable when its merge step chooses from the left half first on equal keys. Python's built-in sorting is also stable and offers a key function; it is generally the better production choice unless the purpose is to teach or implement divide and conquer explicitly. [Python's sorting documentation](https://docs.python.org/3/howto/sorting.html) describes key functions and the stability guarantee.

A full catalog can be too large to fetch and sort for every request. Production systems commonly use database indexes, search services, pagination, and cached query results. The case-study algorithm is a clear model of sorting the candidate set after filtering; it does not claim that a commercial store uses this exact implementation.

## 5. Correctness and quality considerations

- Every eligible product must appear exactly once in the results.
- Prices must be compared numerically, including decimal/currency handling where applicable.
- The selected order must be deterministic for equal prices.
- The store should define how unavailable products, discounts, taxes, and shipping costs affect the displayed price.
- Sorting by price alone must not be presented as a recommendation or relevance ranking.
- Test empty input, one product, already sorted input, reverse-sorted input, repeated prices, and missing or invalid price data.

## 6. Conclusion

Merge sort shows how divide and conquer can order an e-commerce result set efficiently and predictably. It offers O(n log n) time and stability, at the cost of extra memory. For a real store, the central lesson is to define the sorting key and tie-breaking behavior clearly; for a large catalog, indexed or paginated retrieval may be more practical than sorting every product in memory for each request.

## 7. Runnable Python implementation

The accompanying [`ecommerce_product_sorting.py`](ecommerce_product_sorting.py) program implements merge sort and provides a menu to display products, sort by price or rating, add a product, and reset the sample catalog. It uses only the Python standard library.

Run it from this folder with:

```bash
python3 ecommerce_product_sorting.py
```

## References

1. Python Software Foundation, [Sorting Techniques](https://docs.python.org/3/howto/sorting.html).
2. Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., *Introduction to Algorithms*, 4th ed., MIT Press, 2022.
