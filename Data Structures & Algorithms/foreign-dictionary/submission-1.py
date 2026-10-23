from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letters_after = {letter: set() for word in words for letter in word}
        in_degree = {letter: 0 for letter in letters_after}

        for first, second in zip(words, words[1:]):
            shorter_length = min(len(first), len(second))
            if len(first) > len(second) and first[:shorter_length] == second[:shorter_length]:
                return ""
            for first_letter, second_letter in zip(first, second):
                if first_letter != second_letter:
                    if second_letter not in letters_after[first_letter]:
                        letters_after[first_letter].add(second_letter)
                        in_degree[second_letter] += 1
                    break

        queue = deque(letter for letter in in_degree if in_degree[letter] == 0)
        order = []

        while queue:
            letter = queue.popleft()
            order.append(letter)
            for next_letter in letters_after[letter]:
                in_degree[next_letter] -= 1
                if in_degree[next_letter] == 0:
                    queue.append(next_letter)

        return "".join(order) if len(order) == len(letters_after) else ""