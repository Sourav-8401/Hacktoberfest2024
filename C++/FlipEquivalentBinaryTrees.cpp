class Solution {
    bool isFlip(TreeNode* root1, TreeNode* root2) {
        if(root1 == nullptr && root2 == nullptr) return true;
        
        if((root1 != nullptr && root2 == nullptr) || (root1 == nullptr && root2 != nullptr)) return false;

        if (root1->val != root2->val) return false;

        return (isFlip(root1->left, root2->left) && isFlip(root1->right, root2->right)) ||
               (isFlip(root1->left, root2->right) && isFlip(root1->right, root2->left));
    }
public:
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        if(root1 == nullptr && root2 == nullptr) {
            return true;
        }

        return isFlip(root1, root2);
    }
};
