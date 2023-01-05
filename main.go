package main

import (
	"fmt"
)

func main() {
//Proyek Hekel//
//Nomor 1//
  var tahanan1, tahanan2, tahanan3 int
  fmt.Println("Program Tahanan")
  fmt.Print("Masukkan Tahanan 1: ")
  fmt.Scan(&tahanan1)
  fmt.Print("Masukkan Tahanan 2: ")
  fmt.Scan(&tahanan2)
  fmt.Print("Masukkan Tahanan 3: ")
  fmt.Scan(&tahanan3)
  if tahanan1 < 0 || tahanan2 < 0 || tahanan3 < 0{
    fmt.Print("Masukkan tahanan tidak boleh negatif")
  }else{
    fmt.Print(tahanan1 + tahanan2 + tahanan3)
  }  
}