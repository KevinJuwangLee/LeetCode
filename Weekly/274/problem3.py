def asteroidsDestroyed(mass, asteroids):
        #x=[]
        while len(asteroids)>0:
            p=[i for i in asteroids if i <= mass]
            if len(p)==0:
                return False
            mass+=max(p)
            asteroids.remove(max(p))
            #x.append(max(p))
        #print(x)
        return True
