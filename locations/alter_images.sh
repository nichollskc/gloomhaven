#!/bin/sh

find raw -name "*.png" | xargs basename | xargs -I{} convert raw/{} -resize 75% {}

for i in 9 35 36; do
CROSS=$(\
    convert location_"$i".png \
    -format "line 10 10 %[fx:w-10] %[fx:h-10], line 10 %[fx:h-10] %[fx:w-10] 10" \
    info:\
)
    
    
    convert location_$i.png -stroke firebrick3 -strokewidth 10 -draw "$CROSS" location_$i.png
done
