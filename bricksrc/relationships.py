from rdflib import Literal
from .namespaces import A, OWL, RDFS, BRICK, VCARD, UNIT, QUDT, SDO, RDF, S223, BSH, XSD

"""
Defining Brick relationships
"""
relationships = {
    "isReplacedBy": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Is replaced by"),
        "range": BRICK.Entity,
        "domain": BRICK.Entity,
    },
    "hasSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Has QUDT reference"),
        "range": BRICK.Substance,
        "domain": [BRICK.Point, BRICK.Meter],
    },
    "hasQuantity": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Has QUDT reference"),
        RDFS.subPropertyOf: QUDT.hasQuantityKind,
        "range": BRICK.Quantity,
        "domain": BRICK.Point,
    },
    "value": {
        RDFS.subPropertyOf: [QUDT.value, S223.hasValue],
        RDFS.label: Literal("Value"),
        A: [RDF.Property],
        "range": RDFS.Resource,
        "domain": RDFS.Resource,
    },
    "latitude": {
        RDFS.subPropertyOf: SDO.latitude,
        RDFS.label: Literal("Latitude"),
        A: [OWL.ObjectProperty],
        "domain": BRICK.Entity,
        "datatype": BSH.NumericValue,
    },
    "longitude": {
        RDFS.subPropertyOf: SDO.longitude,
        RDFS.label: Literal("Longitude"),
        A: [OWL.ObjectProperty],
        "domain": BRICK.Entity,
        "datatype": BSH.NumericValue,
    },
    "timestamp": {
        RDFS.label: Literal("Timestamp"),
        A: [RDF.Property],
        "domain": BRICK.Entity,
        "datatype": XSD.dateTime,
    },
    "hasQUDTReference": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Has QUDT reference"),
        "domain": BRICK.Quantity,
        "range": QUDT.QuantityKind,
    },
    "isLocationOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasLocation"],
        "domain": BRICK.Location,
        "range": BRICK.Entity,
        RDFS.label: Literal("Is location of"),
    },
    "hasLocation": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isLocationOf"],
        "domain": BRICK.Entity,
        "range": BRICK.Location,
        RDFS.label: Literal("Has location"),
    },
    "hasInputSubstance": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "range": BRICK.Substance,
        "domain": BRICK.Equipment,
        RDFS.label: Literal("Has input substance"),
    },
    "hasOutputSubstance": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "range": BRICK.Substance,
        "domain": BRICK.Equipment,
        RDFS.label: Literal("Has output substance"),
    },
    "feeds": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isFedBy"],
        RDFS.label: Literal("Feeds"),
    },
    "isFedBy": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["feeds"],
        RDFS.label: Literal("Is fed by"),
    },
    "hasPoint": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isPointOf"],
        "range": BRICK.Point,
        "domain": [BRICK.Equipment, BRICK.Location],
        RDFS.label: Literal("Has point"),
    },
    "isPointOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPoint"],
        "domain": BRICK.Point,
        "range": [BRICK.Equipment, BRICK.Location],
        RDFS.label: Literal("Is point of"),
    },
    "hasPart": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isPartOf"],
        RDFS.label: Literal("Has part"),
    },
    "isPartOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPart"],
        RDFS.label: Literal("Is part of"),
    },
    "hasTag": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isTagOf"],
        "range": BRICK.Tag,
        "domain": OWL.Class,
        RDFS.label: Literal("Has tag"),
    },
    "isTagOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "domain": BRICK.Tag,
        "range": OWL.Class,
        RDFS.label: Literal("Is tag of"),
    },
    "hasAssociatedTag": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isAssociatedWith"],
        "domain": OWL.Class,
        "range": BRICK.Tag,
        RDFS.label: Literal("Has associated tag"),
    },
    "isAssociatedWith": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasAssociatedTag"],
        "domain": BRICK.Tag,
        "range": OWL.Class,
        RDFS.label: Literal("Is associated with"),
    },
    "hasAddress": {
        RDFS.subPropertyOf: VCARD.hasAddress,
        "domain": BRICK.Building,
        "range": VCARD.Address,
        RDFS.label: Literal("Has address"),
    },
    "hasUnit": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "range": QUDT.Unit,
        "domain": BRICK.Point,
        RDFS.label: Literal("Has unit"),
    },
    "meters": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK.isMeteredBy,
        "domain": BRICK.Meter,
        # this is a special property that implements the 'range' as a SHACL shape
        "range": [BRICK.Equipment, BRICK.Location, BRICK.Collection],
        RDFS.label: Literal("meters"),
    },
    "isMeteredBy": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK.meters,
        # this is a special property that implements the 'domain' as a SHACL shape
        "domain": [BRICK.Equipment, BRICK.Location, BRICK.Collection],
        "range": BRICK.Meter,
        RDFS.label: Literal("is metered by"),
    },
    "hasSubMeter": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK.isSubMeterOf,
        "range": BRICK.Meter,
        "domain": BRICK.Meter,
        RDFS.label: Literal("has sub-meter"),
    },
    "isSubMeterOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK.hasSubMeter,
        "range": BRICK.Meter,
        "domain": BRICK.Meter,
        RDFS.label: Literal("is sub-meter of"),
    },
}
