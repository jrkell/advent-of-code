
function Open-Input {
    $TextInput = Get-Content -Path "$PSScriptRoot\input.txt"
    $TextInput.Split(",").Trim()
}

function Move-Direction {
    [CmdletBinding()]
    param (
        $Location,
        $Rotation,
        $Distance
    )

    # rotate
    switch ($Location.Facing) {
        "N" { 
            if ($Rotation -eq "L") { $Location.Facing = "W" }
            if ($Rotation -eq "R") { $Location.Facing = "E" }
        }
        "E" { 
            if ($Rotation -eq "L") { $Location.Facing = "N" }
            if ($Rotation -eq "R") { $Location.Facing = "S" }
        }
        "S" { 
            if ($Rotation -eq "L") { $Location.Facing = "E" }
            if ($Rotation -eq "R") { $Location.Facing = "W" }
        }
        "W" { 
            if ($Rotation -eq "L") { $Location.Facing = "S" }
            if ($Rotation -eq "R") { $Location.Facing = "N" }
        }
        Default {}
    }

    # move
    switch ($Location.Facing) {
        "N" { 
            $Location.Y += $Distance
        }
        "E" { 
            $Location.X += $Distance
        }
        "S" { 
            $Location.Y -= $Distance
        }
        "W" { 
            $Location.X -= $Distance
        }
        Default {}
    }
}

function Get-Part1 {
    $InputArray = Open-Input

    $Directions = $InputArray.ForEach{
        [PSCustomObject]@{
            Direction = $_[0]
            Distance = [int32]$_.substring(1, $_.length - 1)
        }
    }
    
    $Location = [PSCustomObject]@{
        Facing = "N"
        X = 0
        Y = 0
    }
    
    $CoOrds = @()

    $Directions.ForEach{
        Move-Direction -Location $Location -Rotation $_.Direction -Distance $_.Distance
        $CoOrds += @($Location.X, $Location.Y)
    }
    
    [Math]::Abs($Location.X) + [Math]::Abs($Location.y)
}


$Part1Answer = Get-Part1
Write-Host "Part 1 Answer: $Part1Answer"

