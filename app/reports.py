from .data import DATA


def get_tools(
    category=None,
    pricing=None,
    sort="rating",
    descending=True,
    offset=0,
    limit=20
):
    results = DATA

    # Filter by category
    if category:
        results = [
            t for t in results
            if t.category == category
        ]

    # Filter by pricing
    if pricing:
        results = [
            t for t in results
            if t.pricing == pricing
        ]

    # Sorting
    results.sort(
        key=lambda t: getattr(t, sort),
        reverse=descending
    )

    # Pagination
    return results[offset: offset + limit]