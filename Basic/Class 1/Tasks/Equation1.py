@@ -0,0 +1,17 @@
+#This equation x2 + y2 + z2 ā€“ 3xyz formula: (x + y + z)(x2 + y2 + z2 ā€“ xy ā€“ yz -xz)
+
+x = int(input("Please provide number x: "))
+y = int(input("Please provide number y: "))
+z = int(input("Please provide number z: "))
+
+#input("Enter :)")
+# total = number1 + number2
+#
+# print("Total of these two numbers is:", total)
+
+#text = input("Provide the text to search in: ")
+#query = input("Provide the text to search for: ")
+total = (x+y+z)*(x**2+y**2+z**2-x*y-y*z-x*z)
+total2 = x*2 + y*2 + z*2 - 3*x*y*z
+print(total, "Result of equation 1")
+print(total2, "Result of equation 2")