class Solution:
    def capitalizeTitle(self, title: str) -> str:
        x=[i.lower() for i in title.split(' ')]
        for i in range(len(x)):
            if len(x[i])>2:
                x[i]=x[i].title()
        return ' '.join(x)