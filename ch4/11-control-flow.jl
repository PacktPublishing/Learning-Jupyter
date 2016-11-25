#Julia Control Flow

function larger(x, y) 
    if (x>y) 
        return x
    end
    return y
end
println(larger(7,8))