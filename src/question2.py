class Orders:
    def combine_orders(self, requests: list, n_max: int):
        requests.sort(reverse=True)
        trips = 0

        start, end = 0, len(requests) - 1
        while start <= end:
            if requests[start] + requests[end] <= n_max:
                end -= 1
            start += 1
            trips += 1

        return trips
