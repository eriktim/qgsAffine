# qgsAffine: Affine Transformations

**Apply affine transformations to selected geometries.**

This Quantim GIS (QGIS) plugin performs affine transformations on layers or a group of features.

## Concept

For those infamiliar with affine transformations, here is the basic concept.

A point `(x,y)` can be tranformed to a new point `(x',y')` by:

    x' = a * x + b * y + tx
    y' = c * x + d * y + ty

where `tx` and `ty` are the translations in the x- and y-direction, resp.  
`a`, `b`, `c` and `d` form the transformation matrix

        | a  b |
    A = |      |
        | c  d |

that determines the rotation and scaling.

`a`, `b`, `c`, `d`, `tx` and `ty` are the variablesthat can be changed in the plugin.  
Details on how to find the correct values for your case can be found anywhere on the Internet.

## Defaults

By default, the translations are zero and `T = I` (the identity matrix), i.e.

    x' = 1 * x + 0 * y + 0 = x
    y' = 0 * x + 1 * y + 0 = y 
