# Test Results

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| Normal input | Scene added successfully, 240 frames calculated | Worked correctly | PASS |
| Text input (abc) | Warning and asks for input again | Worked correctly | PASS |
| Negative duration (-5) | Warning and asks for input again | Worked correctly | PASS |
| Zero FPS (0) | Warning and asks for input again | Worked correctly | PASS |
| Scene listing | Displays added scenes | Worked correctly | PASS |
| CSV saving | Saves scene data to CSV file | Worked correctly | PASS |
| Menu exit | Closes the program | Worked correctly | PASS |

## Bugs Found
No major bugs were found during manual testing.

## Corrections Made
Input validation successfully prevented invalid values from being accepted. The program continued running and requested valid input.
Test

Result

test_kisa_sahne

PASS

test_orta_sahne

PASS

test_uzun_sahne

PASS

test_calisma_gunu

PASS

test_farkli_fps

PASS

Total: 5 tests
Passed: 5
Failed: 0

All automated tests passed successfully.