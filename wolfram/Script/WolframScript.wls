Print["Wolfram Language 12.3.1 Engine"]
Print["Copyright 1988-2021 Wolfram Research, Inc.\n"]
For[i = 1, i < 100000, i++, Print[StringJoin["\nOut[", ToString[i], "]:= ", ToString[Evaluate[Input[StringJoin["In[", ToString[i], "]:= "]]]], "\n"]]]