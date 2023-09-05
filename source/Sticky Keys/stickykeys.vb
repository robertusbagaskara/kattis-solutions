Imports System

Module Program
    Sub Main(args As String())
        Dim s As String = Console.ReadLine()
        Dim substringS As String = ""
        Dim substringSMin1 As String = ""
        Dim trimmedS = ""

        For positionS = 1 To Len(s)
            substringS = Mid(s, positionS, 1)
            If substringS <> substringSMin1 Then
                trimmedS += substringS
            End If
            substringSMin1 = Mid(s, positionS, 1)
        Next

        Console.WriteLine(trimmedS)

    End Sub
End Module
