public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> numberSet = new HashSet<int>(nums);
        if (nums.Length == numberSet.Count){return false;}
        return true;
    }
}