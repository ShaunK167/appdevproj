class Product:
    count_id = 0

    def __init__(self, object_type, condition, collection, weight, quantity, ppu, description, image):
        Product.count_id += 1
        self.__product_id = Product.count_id
        self.__object_type = object_type
        self.__condition = condition
        self.__collection = collection
        self.__weight = weight
        self.__quantity = quantity
        self.__ppu = ppu
        self.__description = description
        self.__image = image
    def get_product_id(self):
        return self.__product_id

    def get_objectType(self):
        return self.__object_type

    def get_condition(self):
        return self.__condition

    def get_collection(self):
        return self.__collection

    def get_weight(self):
        return self.__weight

    def get_quantity(self):
        return self.__quantity

    def get_ppu(self):
        return self.__ppu

    def get_description(self):
        return self.__description

    def get_image(self):
        return self.__image

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_ObjectType(self, object_type):
        self.__object_type = object_type

    def set_condition(self, condition):
        self.__condition = condition

    def set_collection(self, collection):
        self.__collection = collection

    def set_weight(self, weight):
        self.__weight = weight

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_ppu(self, ppu):
        self.__ppu = ppu

    def set_description(self, description):
        self.__description = description

    def set_image(self, image):
        self.__image = image
