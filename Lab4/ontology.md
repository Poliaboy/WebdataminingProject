Classes and Subclasses:
Person

Subclass: Customer
Properties: hasPreference
Business

Subclasses: Restaurant, DeliveryService
Restaurant Properties: offersFoodItem, locatedIn
DeliveryService Properties: deliversFor
Product

Subclasses: FoodItem, Offer
FoodItem Properties: hasCuisineType, hasDietType, partOfOffer
Offer Properties: includesFoodItem, hasDiscount
Order

Properties: orderedBy, containsProduct, deliveredBy, orderFrom
Location (to represent delivery locations, restaurant locations, etc.)

Preference

Subclasses: CuisinePreference, DietPreference
Properties: preferredCuisine, preferredDiet
Relationships (Object Properties):
hasPreference: Person -> Preference
offersFoodItem: Restaurant -> FoodItem
deliversFor: DeliveryService -> Restaurant
partOfOffer: FoodItem -> Offer
includesFoodItem: Offer -> FoodItem
orderedBy: Order -> Customer
containsProduct: Order -> Product
deliveredBy: Order -> DeliveryService
orderFrom: Order -> Restaurant
Data Properties:
hasCuisineType: FoodItem -> xsd:string
hasDietType: FoodItem -> xsd:string
hasDiscount: Offer -> xsd:float
locatedIn: Business -> Location
preferredCuisine: CuisinePreference -> xsd:string
preferredDiet: DietPreference -> xsd:string