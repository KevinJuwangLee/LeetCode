class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        questions=questions[::-1]
        p=0
        u=0
        for i, data in enumerate(questions):
            if i+1-data[1]>u:
                p+=data[0]
                u=i
        return p
