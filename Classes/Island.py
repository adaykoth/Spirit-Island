class Island:
    def __init__(self, fear=0, fearlevel=1, healthy=True, blight=2, turn=0):
        self.fearlevel = fearlevel
        self.fear = fear
        self.healthy = healthy
        self.blight = blight
        self.turn = turn

    def remove_blight(self):
        self.blight -= 1
        if self.blight == 0 and self.healthy:
            # Turn around blight card
            self.blight = 2
            self.healthy = False
            print("  -- The island has become unhealthy  --")
            pass
        elif self.blight == 0 and not self.healthy:
            print("The island has become blighted. It will never recover from this!\n  --  Game Over  --")