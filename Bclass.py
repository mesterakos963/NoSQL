import redis
import uuid
import random


class Borton():
    
    def __init__(self):
        redis_host='192.168.100.19'
        redis_port=6379
        
        self.r=redis.Redis(host=redis_host, 
                           port=redis_port, 
                           decode_responses=True)

    def clean(self):
        self.r.flushdb()
    
    
    def __generate_azon__(self):
        azon = str(uuid.uuid4())
        if self.sismember('h_azon_', azon):
            self.__generate_azon__(self)
        else:
            return azon
    
    
    def __gen_cella__(self):
        cella_szam = random.randint(1,100)
        if self.sismember('s_cella_szam', cella):
            self.__gen_cella__(self)
        else:
            return cella_szam

   
    def __mai_datum__(self):
        return szul_dat = redis.call('TIME')
    
    
    def rab_felvesz(self, nev, nem, szul_dat, bunt_kezd, bunt_veg, azon, cellaszam):
        azon = self.__generate_azon__()
        cella = self.__generate_azon__()
        szul_dat = __mai_datum__()
        self.r.hmset('h_rab_' + azon, {'nev': nev,'nem': nem,'szul_dat': 'szul_dat': szul_dat,'bunt_kezd': bunt_kezd, 'bunt_veg': bunt_veg,'azon': azon,'cella': cellaszam
        self.r.sadd('s_rab_ok', azon)
    
    
    def rab_elenged(self, azon):
        e = self.r.hget(self, nev, nem, szul_dat, bunt_kezd, bunt_veg, azon, cellaszam)
        self.r.hdel(self, nev, nem, szul_dat, bunt_kezd, bunt_veg, azon, cellaszam)
    
    
    def rab_leker(self, azon):
        return self.r.hgetall('_rab_' + azon)
    
    
    def rab_lista(self):
        for i in self.r.smembers('_rabok_'):
            print(self.r.hgetall('_rab_' + i))
    
    
    def rendez_bunt_kezd_szerint(self):
        return self.r.zrevrange('zset_bunt_kezd',0,-1,withscores = True)
    
    
    def rendez_bunt_vege_szerint(self):
        return self.r.zrevrange('zset_bunt_vege',0,-1,withscores = True)
    
    
    def rendez_kor_szerint(self):
        return self.r.zrevrange('zset_kor',0,-1,withscores = True)
    
    
    def nev_lista(self):
        return self.r.smembers('_rabok_')
    
    
    def nev_leker(self, nev):
        return self.r.hgetall('_rabok_' + nev)
    
    
    def azon_lista(self, azon):
        return self.r.hgetall('_rabok_' + azon)
    
    
    def azon_lista(self, azon):
        return self.r.hgetall('_rabok_' + azon, cella_szam)
    
    
    def nem_leker(self, azon):
        return self.r.hgetall('_rabok_' + azon, nev, nem)
    
    
    def kor_leker(self, azon):
        return self.r.hgetall('_rabok_' + azon, nev, kor)