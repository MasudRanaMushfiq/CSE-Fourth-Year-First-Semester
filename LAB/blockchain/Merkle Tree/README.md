
## 📑 **Check Document Integrity using Merkle Tree**

### **Problem Statement**

Data integrity is a critical requirement in distributed systems and blockchain technology. A **Merkle Tree** is used to efficiently and securely verify the integrity of data blocks.

You are tasked to implement a Merkle Tree for a set of documents (or file contents) and verify whether a given document is part of the dataset.

---

### **Tasks**

1. **Construct a Merkle Tree**

   * Split the document(s) into fixed-size chunks or use multiple documents.
   * Compute the SHA-256 hash of each chunk/document.
   * Build the Merkle Tree by recursively hashing pairs of nodes until a single root (Merkle Root) is obtained.

2. **Display the Merkle Root**

   * Print the final Merkle Root of the dataset.

3. **Verify Document Integrity**

   * For a given document, generate a **Merkle Proof** (hash path from the document to the root).
   * Verify whether the document belongs to the original dataset by checking if the calculated root matches the stored Merkle Root.

4. **Simulate Tampering**

   * Modify one document slightly and show how the verification fails.

---

### **Expected Output**

* Display of leaf node hashes.
* Intermediate hashes up to the Merkle Root.
* Merkle Root value.
* Verification result:

  * ✅ "Document is authentic" if unchanged.
  * ❌ "Document integrity failed" if modified.

---