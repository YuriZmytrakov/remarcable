import os
import django
from django.utils.text import slugify

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "remarcable.settings")
django.setup()

from products.models import Product, Category, Tag


def create_products():
    categories = {
        "Electrical Supplies": Category.objects.get_or_create(
            name="Electrical Supplies",
        )[0],
        "Plumbing & Piping": Category.objects.get_or_create(
            name="Plumbing & Piping",
        )[0],
        "HVAC & Ventilation": Category.objects.get_or_create(
            name="HVAC & Ventilation",
        )[0],
        "Tools & Equipment": Category.objects.get_or_create(
            name="Tools & Equipment",
        )[0],
        "Fasteners & Adhesives": Category.objects.get_or_create(
            name="Fasteners & Adhesives",
        )[0],
    }

    # Create tags
    tags = {
        "Heavy-duty": Tag.objects.get_or_create(
            name="Heavy-duty",
        )[0],
        "Certified": Tag.objects.get_or_create(
            name="Certified",
        )[0],
        "Quick-install": Tag.objects.get_or_create(
            name="Quick-install",
        )[0],
        "Waterproof": Tag.objects.get_or_create(
            name="Waterproof",
        )[0],
        "Energy-efficient": Tag.objects.get_or_create(
            name="Energy-efficient",
        )[0],
        "Compact": Tag.objects.get_or_create(
            name="Compact",
        )[0],
        "Industrial-grade": Tag.objects.get_or_create(
            name="Industrial-grade",
        )[0],
        "Fire-resistant": Tag.objects.get_or_create(
            name="Fire-resistant",
        )[0],
        "Eco-friendly": Tag.objects.get_or_create(
            name="Eco-friendly",
        )[0],
        "Low-maintenance": Tag.objects.get_or_create(
            name="Low-maintenance",
        )[0],
    }

    # Product data
    products = [
        {
            "name": "12-Gauge Electrical Wire Roll",
            "category": categories["Electrical Supplies"],
            "tags": [tags["Heavy-duty"], tags["Certified"]],
            "description": "Durable 12-gauge copper wire suitable for residential and commercial wiring. Meets electrical code standards for safety and performance in demanding environments.",
            "price": 89.99,
            "stock": 150,
        },
        {
            "name": "PEX Pipe – 1/2 inch, 100ft",
            "category": categories["Plumbing & Piping"],
            "tags": [tags["Quick-install"], tags["Waterproof"]],
            "description": "Flexible and kink-resistant PEX pipe ideal for hot and cold water supply lines. Easy to install with minimal fittings and excellent long-term reliability.",
            "price": 129.99,
            "stock": 75,
        },
        {
            "name": "Mini Split AC Unit – 12,000 BTU",
            "category": categories["HVAC & Ventilation"],
            "tags": [tags["Energy-efficient"], tags["Compact"]],
            "description": "High-efficiency ductless mini split system for room-by-room climate control. Features quiet operation, remote control, and a compact indoor unit.",
            "price": 899.99,
            "stock": 25,
        },
        {
            "name": "Cordless Power Drill – 20V",
            "category": categories["Tools & Equipment"],
            "tags": [tags["Heavy-duty"], tags["Industrial-grade"]],
            "description": "Powerful 20V cordless drill with variable speed and long-lasting battery life. Built for daily use in demanding job site conditions.",
            "price": 159.99,
            "stock": 40,
        },
        {
            "name": "Copper Fittings Assortment Kit",
            "category": categories["Plumbing & Piping"],
            "tags": [tags["Fire-resistant"], tags["Certified"]],
            "description": "A 50-piece kit of copper elbows, tees, and couplings for soldered or press-fit plumbing applications. Fire-resistant and compliant with building codes.",
            "price": 49.99,
            "stock": 60,
        },
        {
            "name": "LED Work Light – Rechargeable",
            "category": categories["Tools & Equipment"],
            "tags": [tags["Eco-friendly"], tags["Compact"]],
            "description": "Portable LED work light with rechargeable battery. Bright, efficient, and space-saving — ideal for low-light workspaces and mobile setups.",
            "price": 39.99,
            "stock": 90,
        },
        {
            "name": "PVC Cement – Fast Set (500ml)",
            "category": categories["Fasteners & Adhesives"],
            "tags": [tags["Quick-install"], tags["Waterproof"]],
            "description": "Industrial-grade PVC adhesive for bonding pipes and fittings. Fast-setting, water-resistant, and suitable for pressure systems.",
            "price": 12.99,
            "stock": 200,
        },
        {
            "name": "Threaded Rod – 3/8 inch x 10 ft",
            "category": categories["Fasteners & Adhesives"],
            "tags": [tags["Industrial-grade"], tags["Heavy-duty"]],
            "description": "Zinc-plated steel threaded rod for use in anchoring, mounting, and bracing systems. Strong and corrosion-resistant.",
            "price": 8.99,
            "stock": 180,
        },
        {
            "name": "Digital Multimeter – CAT III 600V",
            "category": categories["Electrical Supplies"],
            "tags": [tags["Certified"], tags["Low-maintenance"]],
            "description": "Professional multimeter for measuring voltage, current, and resistance. CAT III rated for commercial applications, with backlit display and auto shut-off.",
            "price": 79.99,
            "stock": 35,
        },
        {
            "name": "Roof Vent – 4 inch Galvanized Steel",
            "category": categories["HVAC & Ventilation"],
            "tags": [tags["Fire-resistant"], tags["Eco-friendly"]],
            "description": "Durable galvanized vent for roof exhaust systems. Fire-resistant and weatherproof — improves airflow in attics and crawlspaces.",
            "price": 24.99,
            "stock": 70,
        },
        {
            "name": "Electric Conduit Bender – Handheld",
            "category": categories["Electrical Supplies"],
            "tags": [tags["Heavy-duty"], tags["Quick-install"]],
            "description": "Compact handheld bender for EMT and rigid conduits. Enables accurate bends on-site with minimal effort.",
            "price": 149.99,
            "stock": 30,
        },
        {
            "name": "HVAC Aluminum Tape – 50m Roll",
            "category": categories["HVAC & Ventilation"],
            "tags": [tags["Waterproof"], tags["Fire-resistant"]],
            "description": "High-tack aluminum foil tape for sealing ductwork and insulation. Withstands extreme temperatures and resists moisture.",
            "price": 18.99,
            "stock": 120,
        },
        {
            "name": "Adjustable Pipe Wrench – 18 inch",
            "category": categories["Tools & Equipment"],
            "tags": [tags["Industrial-grade"], tags["Heavy-duty"]],
            "description": "Heavy-duty adjustable pipe wrench with forged steel jaws. Ideal for gripping and turning threaded pipe and fittings.",
            "price": 44.99,
            "stock": 55,
        },
        {
            "name": "Expandable Foam Sealant – 750ml",
            "category": categories["Fasteners & Adhesives"],
            "tags": [tags["Waterproof"], tags["Low-maintenance"]],
            "description": "One-component polyurethane foam that expands to fill gaps and cracks. Cures quickly, resists water, and insulates well.",
            "price": 14.99,
            "stock": 150,
        },
        {
            "name": "Electrical Box – Weatherproof Surface Mount",
            "category": categories["Electrical Supplies"],
            "tags": [tags["Waterproof"], tags["Fire-resistant"]],
            "description": "Rugged outdoor-rated electrical box with gasket seal. Built to protect wiring connections in exposed environments.",
            "price": 9.99,
            "stock": 200,
        },
        {
            "name": "Thermostat – Smart Wi-Fi Enabled",
            "category": categories["HVAC & Ventilation"],
            "tags": [tags["Energy-efficient"], tags["Eco-friendly"]],
            "description": "Programmable smart thermostat compatible with Alexa and Google Home. Helps reduce energy costs through learning algorithms and remote control.",
            "price": 199.99,
            "stock": 20,
        },
        {
            "name": "Anchor Bolt Kit – 50 pcs",
            "category": categories["Fasteners & Adhesives"],
            "tags": [tags["Certified"], tags["Heavy-duty"]],
            "description": "Concrete anchor bolts with washers and nuts for secure fastening. Certified for structural applications and seismic zones.",
            "price": 29.99,
            "stock": 80,
        },
        {
            "name": "Heat Gun – Variable Temperature",
            "category": categories["Tools & Equipment"],
            "tags": [tags["Industrial-grade"], tags["Compact"]],
            "description": "Multi-purpose heat gun with adjustable temperature settings. Ideal for stripping paint, shrinking tubing, and thawing pipes.",
            "price": 59.99,
            "stock": 45,
        },
        {
            "name": 'Ball Valve – Brass 1"',
            "category": categories["Plumbing & Piping"],
            "tags": [tags["Low-maintenance"], tags["Certified"]],
            "description": "Full-port brass ball valve for residential or commercial water systems. Corrosion-resistant and maintenance-free.",
            "price": 34.99,
            "stock": 65,
        },
        {
            "name": "Caulking Gun – Heavy-Duty Manual",
            "category": categories["Tools & Equipment"],
            "tags": [tags["Quick-install"], tags["Heavy-duty"]],
            "description": "Manual caulking gun with smooth trigger action for controlled application of sealants and adhesives.",
            "price": 19.99,
            "stock": 100,
        },
    ]

    for product_data in products:
        product = Product.objects.create(
            name=product_data["name"],
            slug=slugify(product_data["name"]),
            description=product_data["description"],
            price=product_data["price"],
            stock=product_data["stock"],
        )
        product.categories.add(product_data["category"])
        for tag in product_data["tags"]:
            product.tags.add(tag)


if __name__ == "__main__":
    create_products()
