package org.IDFM

/**
 * @author ${user.name}
 */
object App {
  
  def foo(x : Array[String]) = x.foldLeft("")((a,b) => a + b)

  var list:Array[String] = new Array[String](3)

  list = Array("caca", "pipi", "prout")

  def main(args : Array[String]) {
    println( "Hello World!" )
    println("concat arguments = " + foo(list))
  }

}
