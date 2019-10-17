using Test
using NumericalRecipes


@testset "test_betacf" begin include("Ch6_SpecialFunctions/betacf/test_betacf.jl") end
@testset "test_betai" begin include("Ch6_SpecialFunctions/betai/test_betai.jl") end
@testset "test_gamma" begin include("Ch6_SpecialFunctions/gammaln/test_gammaln.jl") end
@testset "test_avevar" begin include("Ch13_StatisticalDescriptionOfData/avevar/test_avevar.jl") end
