from bank import bank

class residential:
    def __init__(self, price, house_price, color_group, rent):
        self.color_group = color_group
        self.rent = rent
        self.price = price
        self.house_price = house_price
        self.owner = None
        self.level = 0

    def landing(self, player):
        if self.owner == None:
            player.buy_possibility()
        elif self.owner == player:
            pass
        else:
            pass


class utility:
    def __init__(self):
        self.price = 150
        self.owner = None

    def landing(self, player):
        if self.owner == None:
            player.buy_possibility()
        elif self.owner == player:
            pass
        else:
            pass


class railroad:
    def __init__(self):
        self.price = 200
        self.owner = None

    def landing(self, player):
        if self.owner == None:
            player.buy_possibility()
        elif self.owner == player:
            pass
        else:
            pass


class tax:
    def __init__(self, amount):
        self.amount = amount

    def landing(self, player):
        player.cash -= self.amount
        player.last_payment


class draw:
    def __init__(self, pile):
        self.pile = pile
    def landing(self, player):
        pass


class jail:
    def __init__(self):
        pass
    def landing(self, player):
        pass



class free_parking:
    def __init__(self):
        pass
    def landing(self, player):
        pass


class go_to_jail:
    def __init__(self):
        pass
    def landing(self, player):
        pass


class start:
    def __init__(self):
        pass

    def landing(self, player):
        pass


class _board:
    def __init__(self, tiles):
        self.tiles = tiles

    def __iter__(self):
        return iter(self.tiles)

    def __getitem__(self, key):
        return self.tiles[key]


# fmt:off
parkveien           = residential(60,  50,  "brown",      [2,  4,   10,  30,  90,   160,  250])
kirkeveien          = residential(60,  50,  "brown",      [4,  8,   20,  60,  180,  320,  450])
kongens_gate        = residential(100, 50,  "light_blue", [6,  12,  30,  90,  270,  400,  550])
prinsens_gate       = residential(100, 50,  "light_blue", [6,  12,  30,  90,  270,  400,  550])
ovre_slottsgate     = residential(120, 50,  "light_blue", [8,  16,  40,  100, 300,  450,  600])
nedre_slottsgate    = residential(140, 100, "pink",       [10, 20,  50,  150, 450,  625,  750])
trondheimsveien     = residential(140, 100, "pink",       [10, 20,  50,  150, 450,  625,  750])
nobels_gate         = residential(160, 100, "pink",       [12, 24,  60,  180, 500,  700,  900])
grensen             = residential(180, 100, "orange",     [14, 28,  70,  200, 550,  750,  950])
gabels_gate         = residential(180, 100, "orange",     [14, 28,  70,  200, 550,  750,  950])
ringgata            = residential(200, 100, "orange",     [16, 32,  80,  220, 600,  800,  1000])
bygdoy_alle         = residential(220, 150, "red",        [18, 36,  90,  250, 700,  875,  1050])
skarpsno            = residential(220, 150, "red",        [18, 36,  90,  250, 700,  875,  1050])
slemdal             = residential(240, 150, "red",        [20, 40,  100, 300, 750,  925,  1100])
karl_johans_gate    = residential(260, 150, "yellow",     [22, 44,  110, 330, 800,  975,  1150])
stortorget          = residential(260, 150, "yellow",     [22, 44,  110, 330, 800,  975,  1150])
torggata            = residential(280, 150, "yellow",     [24, 48,  120, 360, 850,  1025, 1200])
trosterudveien      = residential(300, 200, "green",      [26, 52,  130, 390, 900,  1100, 1275])
pilestredet         = residential(300, 200, "green",      [26, 52,  130, 390, 900,  1100, 1275])
sinsen              = residential(320, 200, "green",      [28, 56,  150, 450, 1000, 1200, 1400])
ulleval_hageby      = residential(350, 200, "navy",       [35, 70,  175, 500, 1100, 1300, 1500])
radhusplassen       = residential(400, 200, "navy",       [50, 100, 200, 600, 1400, 1700, 2000])

oslo_s              = railroad()
skøyen_s            = railroad()
grorud_s            = railroad()
bryn_s              = railroad()

vannverket          = utility()
oslo_energi         = utility()

formueskatt         = tax(200)
luksusskatt         = tax(100)

prov_lykken1        = draw('prov_lykken')
prov_lykken2        = draw('prov_lykken')
prov_lykken3        = draw('prov_lykken')
sjanse1             = draw('sjanse')
sjanse2             = draw('sjanse')
sjanse3             = draw('sjanse')

start = start()
jail = jail()
free_parking = free_parking()
go_to_jail = go_to_jail()
# fmt:on

board = _board(
    (
        start,
        parkveien,
        prov_lykken1,
        kirkeveien,
        formueskatt,
        oslo_s,
        kongens_gate,
        sjanse1,
        prinsens_gate,
        ovre_slottsgate,
        jail,
        nedre_slottsgate,
        oslo_energi,
        trondheimsveien,
        nobels_gate,
        skøyen_s,
        grensen,
        prov_lykken2,
        gabels_gate,
        ringgata,
        free_parking,
        bygdoy_alle,
        sjanse2,
        skarpsno,
        slemdal,
        grorud_s,
        karl_johans_gate,
        stortorget,
        vannverket,
        torggata,
        go_to_jail,
        trosterudveien,
        pilestredet,
        prov_lykken3,
        sinsen,
        bryn_s,
        sjanse3,
        ulleval_hageby,
        luksusskatt,
        radhusplassen,
    )
)
