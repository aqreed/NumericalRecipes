# Contains the function(s): avevar

function avevar(data)
    # Given an array "data" of length "n", returns
    # its mean "ave" and its variance "var"
    n = length(data)
    ave, var = 0, 0

    # Mean
    for i = 1:n
        ave =  ave + data[i]
    end

    ave = ave / n

    # Variance (of a sample population)
    for i = 1:n
        s = data[i] - ave
        var =  var + s^2
    end

    var = var / (n - 1)

    return ave, var
end
