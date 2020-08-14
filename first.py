
def peak(arr):
        n=len(arr)
        longestpeak=0
        i=1
        while i<n-1:
                if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                        pass
                else:
                        i=i+1
                        continue

                left=i-2
                while left>=0 and arr[left]<arr[left+1]:
                        left=left-1
                
                right=i+2
                while right<len(arr) and arr[right]<arr[right-1]:
                        right=right+1

                current=right-left-1
                longestpeak=max(longestpeak,current)
                i=right
        return longestpeak




n=int(input("Enter number of elements of array: "))
print("Enter elements :")
arr=[]
for i in range(0,n):
        z=int(input())
        arr.append(z)

a=peak(arr)
if(a==0):
        print("No peak found")
else:
        print("Longest Peak is :",a)


