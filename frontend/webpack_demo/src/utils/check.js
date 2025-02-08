export const checkPhone = (phone) => {
  if (phone.length !== 11) {
    return false;
  }
  if (phone[0] !== '1') {
    return false;
  }
  for (let i = 1; i < phone.length; i++) {
    if (phone[i] < '0' || phone[i] > '9') {
      return false;
    }
  }
  return true;
}

