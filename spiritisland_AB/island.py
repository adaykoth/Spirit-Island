class Island:
    def __init__(self, lands):
        self.lands = lands

    def __repr__(self):
        value = "Island:\n"
        for land in self.lands:
            value += f"\t{land}\n"
        return value

    def show(self):
        print(self)

    def explore(self, landType):
        print(f"Explore Phase: {landType.name}")
        for land in self.lands:
            if land.landType == landType:
                land.explore()
        self.show()

    def build(self, landType):
        print(f"Build Phase: {landType.name}")
        for land in self.lands:
            if land.landType == landType:
                land.build()
        self.show()

    def ravage(self, landType):
        print(f"Ravage Phase: {landType.name}")
        for land in self.lands:
            if land.landType == landType:
                land.ravage()
        self.show()
