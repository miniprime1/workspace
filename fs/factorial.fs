open System

let rec fact x =
   if x < 1 then 1
   else x * fact (x - 1)

[<EntryPoint>]
let main argv =
    for i = 1 to 10 do
       printfn "%d! = %d" i (fact i)
    0
