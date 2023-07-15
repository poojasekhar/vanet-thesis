double cbrfuncpower(int density, int txpower)
{
    double cbr;

    if (txpower == 2)
        cbr = (0.0137 * density) + 0.0911;
    else if (txpower == 4)
        cbr = (0.0156 * density) + 0.129;
    else if (txpower == 6)
        cbr = (0.0163 * density) + 0.1502;
    else if (txpower == 8)
        cbr = (0.0165 * density) + 0.1553;
    else if (txpower == 10)
        cbr = (0.0165 * density) + 0.1553;
    else if (txpower == 12)
        cbr = (0.0165 * density) + 0.155;
    else if (txpower == 14)
        cbr = (0.0164 * density) + 0.1559;
    else if (txpower == 16)
        cbr = (0.0165 * density) + 0.1556;
    else if (txpower == 18)
        cbr = (0.0165 * density) + 0.1557;
    else if (txpower == 20)
        cbr = (0.0165 * density) + 0.1552;
    else
        cbr = -1;

    if (cbr > 0.92)
        cbr = 0.92;

    return cbr;
}
