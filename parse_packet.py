#!/usr/bin/python
import sys
import gzip
import xlsxwriter

if len(sys.argv) != 3:
    print ("input file required")
    exit()

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
enum_req_r = [
    'Control',
    'Data',
    'Request_Control',
    'Reissue_Control',
    'Response_Data',
    'ResponseL2hit_Data',
    'ResponseLocal_Data',
    'Response_Control',
    'Writeback_Data',
    'Writeback_Control',
    'Broadcast_Control',
    'Multicast_Control',
    'Forwarded_Control',
    'Invalidate_Control',
    'Unblock_Control',
    'Persistent_Control',
    'Completion_Control',
    'SPECLD_Control',
    'SPECLD_Request_Control',
    'SPECLD_Data',
    'EXPOSE_Control',
    'EXPOSE_Request_Control',
    'EXPOSE_Data',
        ]
req_rows = {
        'Control'                : 1,
        'Data'                   : 2,
        'Request_Control'        : 3,
        'Reissue_Control'        : 4,
        'Response_Data'          : 5,
        'ResponseL2hit_Data'     : 6,
        'ResponseLocal_Data'     : 7,
        'Response_Control'       : 8,
        'Writeback_Data'         : 9,
        'Writeback_Control'      : 10,
        'Broadcast_Control'      : 11,
        'Multicast_Control'      : 12,
        'Forwarded_Control'      : 13,
        'Invalidate_Control'     : 14,
        'Unblock_Control'        : 15,
        'Persistent_Control'     : 16,
        'Completion_Control'     : 17,
        'SPECLD_Control'         : 18,
        'SPECLD_Request_Control' : 19,
        'SPECLD_Data'            : 20,
        'EXPOSE_Control'         : 21,
        'EXPOSE_Request_Control' : 22,
        'EXPOSE_Data'            : 23,
}
enum_req_c = [
        "L1Cache",
        "L2Cache",
        "L3Cache",
        "Directory",
        "DMA",
        "Collector",
        "L1Cache_wCC",
        "L2Cache_wCC",
        "CorePair",
        "TCP",
        "TCC",
        "TCCdir",
        "SQC",
        "RegionDir",
        "RegionBuffer",
        "NULL",
        ]

req_cols = {
        "L1Cache":      1,
        "L2Cache":      2,
        "L3Cache":      3,
        "Directory":    4,
        "DMA":          5,
        "Collector":    6,
        "L1Cache_wCC":  7,
        "L2Cache_wCC":  8,
        "CorePair":     9,
        "TCP":          10,
        "TCC":          11,
        "TCCdir":       12,
        "SQC":          13,
        "RegionDir":    14,
        "RegionBuffer": 15,
        "NULL":         16,
        }

def process_line(msg):

    print 'process msg: ' + msg
    msg = " ".join(msg.split())
    print 'msg: ' + msg


    requestor = (msg.split(" ")[0]).split("::")[1]
    data = int(msg.split(" ")[1])


    idx_req = msg.find("message_size_type")
    idx_del = msg.find("::")
    type = int(msg[idx_req+22:idx_del])

    print ("type: %s, fr: %s, data: %d" %(type, requestor, data))
    return type, requestor, data


def update_dictionary(dic, enum, type, fr, data):
    if !dic.has_key(enum[type]):
        dic[enum[type]] = {}

    print("update %s, %s" % (enum[type], fr))
    dic[enum[type]][fr] = data




requests = {}
with open(input_file_name, 'rb') as f:
    stat_cnt = 0
    for line in f:
        if line.find("sim_ticks") != -1:
            stat_cnt += 1
        if stat_cnt > 1:
            break
        if line.find("system.ruby.network.message_size_type_req") != -1:
            if line.find('total') != -1:
                continue
            type, requestor, data = process_line(line)
            update_dictionary(requests, enum_req_r, type, requestor, data)

print requests

response = {}
with open(input_file_name, 'rb') as f:
    stat_cnt = 0
    for line in f:
        if line.find("sim_ticks") != -1:
            stat_cnt += 1
        if stat_cnt > 1:
            break
        if line.find("system.ruby.network.message_size_type_res") != -1:
            if line.find('total') != -1:
                continue
            type, requestor, data = process_line(line)
            update_dictionary(response, enum_req_r, type, requestor, data)
print response


# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(output_file_name)
ws = respons = workbook.add_worksheet()

ws.write(0,0, 'REQUEST')
row = 1
for req in enum_req_r:
    ws.write(row, 0, req)
    row += 1

col = 1
for requestor in enum_req_c:
    ws.write(0, col, requestor)
    col += 1

for event, req_cnt  in requests.iteritems():
    for req, num_req in req_cnt.iteritems():
        #print event
        #print req
        #print num_req
        ws.write(req_rows[event], req_cols[req], num_req)


ws.write(30,0, 'RESPONSE')
row = 1
for res in enum_req_r:
    ws.write(row+30, 0, res)
    row += 1

col = 1
for responsor in enum_req_c:
    ws.write(0, col, responsor)
    col += 1

for event, res_cnt  in response.iteritems():
    for res, num_res in res_cnt.iteritems():
        #print event
        #print req
        #print num_req
        ws.write(req_rows[event]+30, req_cols[res], num_res)

workbook.close()
