/*
 * Complete the 'bonAppetit' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY bill
 *  2. INTEGER k
 *  3. INTEGER b
 */

fn bon_appetit(bill: &[i32], k: i32, b: i32) {
    // bill = array of integers representing the cost of each item ordered
    // k = integer representing the zero-based index of the item Anna doesn't eat
    // b = the amount of money that Anna contributed to the bill
    
    println!("bill = {:?}", bill);
    let item = &bill[k as usize];
    let mut anna_total: i32 = 0;
    let mut anna_count: i32 = 0;
    let anna_bill :f32;
    let mut brian_total: i32 = 0;
    let brian_bill: f32;

    for i in bill {
        if i != item {
            anna_total += i;
            anna_count += 1;
        }
        brian_total += i;
    }

    anna_bill = anna_total as f32 / 2 as f32;
    brian_bill = brian_total as f32 / bill.len() as f32;
    println!("Anna total: {}, count: {},  bill: {}", anna_total, anna_count, anna_bill);
    println!("Brian total: {}, count: {}, bill: {}", brian_total, bill.len(), brian_bill);

    let refund: f32 = b as f32 - anna_bill;
    println!("Anna refund: {}", refund);

    // println!("bill = {:?}", his);
    // println!("slice = {}", item);
}

fn print_bill(bill: &[i32]) {
    for i in bill {
        print!("{}, ", i);
    }
}

fn main() {
    let bill: [i32; 4] = [3, 10, 2, 9]; 
    let k: i32 = 1;
    let b: i32 = 12;
    bon_appetit(&bill, k, b);
 }