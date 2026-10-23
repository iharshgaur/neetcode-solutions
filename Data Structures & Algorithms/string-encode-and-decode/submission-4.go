type Solution struct{}

// Encode joins the strings, prefixing each with its length and a '#'
func (s *Solution) Encode(strs []string) string {
	encoded := ""
	for i := 0; i < len(strs); i++ {
		// Example: "neet" becomes "4#neet"
		encoded += strconv.Itoa(len(strs[i])) + "#" + strs[i]
	}
	return encoded
}

// Decode extracts the strings using the length prefixes
func (s *Solution) Decode(encoded string) []string {
	decoded := []string{}
	i := 0

	for i < len(encoded) {
		// Find the delimiter '#'
		j := i
		for encoded[j] != '#' {
			j++
		}

		// The characters before '#' are the length
		lengthStr := encoded[i:j]
		length, _ := strconv.Atoi(lengthStr)

		// The string starts exactly after the '#'
		start := j + 1
		end := start + length
		
		// Extract the exact word and append
		decoded = append(decoded, encoded[start:end])

		// Move the pointer 'i' to the end of the current word
		i = end
	}

	return decoded
}
