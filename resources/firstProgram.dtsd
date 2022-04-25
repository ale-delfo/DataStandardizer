Source: resources/titanic.csv (csv)
Destination: output (json) overwrite

+ Cast(Fare -> INT)
//+ Deduplicate(Sex) order by Parents/Children_Aboard desc
+ CreateLiteral(LiteralColumn)("1650644337")
+ CreateLiteral(Timezone)("Europe/Rome")
+ Cast(LiteralColumn -> LONG)
+ Cast(LiteralColumn -> INT)
//+ RenameColumn(Sex -> Sesso)
+ FromUnixtime(s)(LiteralColumn)
+ OutputPartitions(Survived)